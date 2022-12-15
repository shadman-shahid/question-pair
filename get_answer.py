from haystack.document_stores import FAISSDocumentStore
from haystack.nodes import EmbeddingRetriever
from haystack.nodes import Seq2SeqGenerator
import pickle
from haystack.pipelines import GenerativeQAPipeline



def load_models():
    document_store = FAISSDocumentStore.load("documents_updated.faiss")
    retriever = EmbeddingRetriever(
        document_store=document_store,
        embedding_model="./all_datasets_v3_mpnet-base",
        model_format="sentence_transformers"
    )
    # generator = pickle.load(open("generator_win.pkl", "rb"))
    generator = Seq2SeqGenerator(model_name_or_path="vblagoje/bart_lfqa")
    pipe = GenerativeQAPipeline(generator, retriever)

    return pipe

def get_answer(query, pipe):
    result = pipe.run(
        query=query,
        params={
            "Retriever": {"top_k": 3},
            "Generator": {"top_k": 1}
        })

    return result["answers"][0].answer






