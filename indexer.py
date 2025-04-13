from collections import defaultdict

STOPWORDS = {
    "the", "is", "and", "or", "a", "an", "of", "in", "on", "to", "for", "with", "by", "there"
}

class InMemoryIndexer:
    def __init__(self):
        self.index = defaultdict(set)
        self.documents = {}

    def add_document(self, document):
        self.documents[document.doc_id] = document
        for token in document.content.lower().split():
            if token not in STOPWORDS:
                self.index[token].add(document.doc_id)

    def search(self, query):
        terms = [t for t in query.lower().split() if t not in STOPWORDS]
        if not terms:
            return set()
        results = self.index.get(terms[0], set()).copy()
        for term in terms[1:]:
            results &= self.index.get(term, set())
        return results
