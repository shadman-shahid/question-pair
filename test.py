# import os
# import time
#
# from haystack.document_stores import ElasticsearchDocumentStore
#
# # Wait 30 seconds only to be sure Elasticsearch is ready before continuing
# time.sleep(30)
#
# # Get the host where Elasticsearch is running, default to localhost
# host = os.environ.get("ELASTICSEARCH_HOST", "localhost")
#
# document_store = ElasticsearchDocumentStore(
#     host=host,
#     username="",
#     password="",
#     index='haystack-lfqa',
#     similarity="cosine",
#     embedding_dim=768
# )

import os
from subprocess import Popen, PIPE, STDOUT
import time
es_server = Popen(
    ["elasticsearch-7.9.2/bin/elasticsearch"], stdout=PIPE, stderr=STDOUT, start_new_session=True  # as daemon
)
# wait until ES has started
time.sleep(30)