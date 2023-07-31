```java
package com.plus.appzenx;

import io.appwrite.Client;
import io.appwrite.services.Events;
import io.appwrite.exceptions.AppwriteException;

public class EventHandlers {

    private Client client;
    private Events events;

    public EventHandlers(Client client) {
        this.client = client;
        this.events = new Events(client);
    }

    public void onUserAuthenticationStatusChange(String userId, String sessionToken) {
        try {
            events.create(userId, sessionToken);
        } catch (AppwriteException e) {
            System.out.println(e.getMessage());
        }
    }

    public void onDatabaseRecordChange(String collectionId, String documentId) {
        try {
            events.create(collectionId, documentId);
        } catch (AppwriteException e) {
            System.out.println(e.getMessage());
        }
    }

    public void onFileUpload(String fileId) {
        try {
            events.create(fileId);
        } catch (AppwriteException e) {
            System.out.println(e.getMessage());
        }
    }

    public void onFileDownload(String fileId) {
        try {
            events.create(fileId);
        } catch (AppwriteException e) {
            System.out.println(e.getMessage());
        }
    }

    public void onFileDeletion(String fileId) {
        try {
            events.create(fileId);
        } catch (AppwriteException e) {
            System.out.println(e.getMessage());
        }
    }
}
```