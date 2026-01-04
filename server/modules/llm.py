from langchain_groq import ChatGroq
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_core.prompts import PromptTemplate
from config import GROQ_API_KEY, PINECONE_API_KEY, GOOGLE_API_KEY


def get_llm_chain(retriever):
    try:
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is missing.")

        # Initialize LLM
        llm = ChatGroq(
            model="llama3-70b-8192",
            groq_api_key=GROQ_API_KEY
        )

        # Define Prompt
        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
                You are **MediBot**, an AI-powered assistant trained to help users understand medical documents and health-related questions.

                Your job is to provide clear, accurate, and helpful responses based **only on the provided context**.

                ---

                🔍 **Context**:
                {context}

                🙋‍♂️ **User Question**:
                {question}

                ---

                💬 **Answer**:
                - Respond in a calm, factual, and respectful tone.
                - Use simple explanations when needed.
                - If the context does not contain the answer, say:
                "I'm sorry, but I couldn't find relevant information in the provided documents."
                - Do NOT make up facts.
                - Do NOT give medical advice or diagnoses.
                """
                        )
        
        # Create RetrievalQA Chain
        qa_chain=RetrievalQA.from_chain_type(
                    llm=llm,
                    chain_type="stuff", 
                    retriever=retriever, 
                    chain_type_kwargs={"prompt": prompt},
                    return_source_documents=True)

        return qa_chain

    except Exception as e:
        raise ValueError(
            "Failed to initialize ChatGroq LLM. "
            "Please check your GROQ API KEY and model configuration."
        ) from e
