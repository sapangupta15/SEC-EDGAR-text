"""
    elasticsearch_document: document in a format that can be loaded into elasticsearch

"""
import json

class ElasticSearchDocument(object):
    def __init__(self):
        self.text = ''
    

    # company_id, document_group, document_type, extraction_method, 
    # sec_cik, sec_company_name, sec_filing_date, sec_url, sec_period_of_interest
    def generate_document_from10k(self, doc_metadata, doc_text):
        self.company_id = doc_metadata.company_id
        self.company_name = doc_metadata.sec_company_name
        self.filing_date = doc_metadata.sec_filing_date
        self.document_group = doc_metadata.document_group
        self.document_type = doc_metadata.document_type
        self.cik = doc_metadata.cik
        self.period_of_interest = doc_metadata.sec_period_of_interest
        self.doc_extension = doc_metadata.extraction_method
        self.doc_url = doc_metadata.sec_url
        self.doc_text = doc_text
        return json.dumps(self)
