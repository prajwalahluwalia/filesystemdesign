Problem Statement
Implement a Simple document Service:
- A document has string content.
- All documents are private when created only the user who creates the document has access for reading/editing the document by default.
-Only the owners of documents can grant {read/edit} access to other users. No user should be able to grant access for a document if he is not the creator of the document.
-Only the owner can delete a document.



document = will store the list of documents with the corresponding owner id
