def test_index_and_search():
    indexer = InMemoryIndexer()
    indexer.add_document(Document("1", "Hello world"))
    indexer.add_document(Document("2", "Hello there"))  # "there" is a stopword
    results = indexer.search("Hello")
    assert "1" in results and "2" in results  # ✅ still passes

    results = indexer.search("there")
    assert results == set()  # ✅ because "there" is a stopword
