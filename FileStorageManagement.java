```java
package com.plus.appzenx;

import io.appwrite.Client;
import io.appwrite.services.Storage;
import com.google.appinventor.components.annotations.*;
import com.google.appinventor.components.runtime.*;
import com.google.appinventor.components.common.ComponentCategory;

@DesignerComponent(version = 1, description = "Extension for Appwrite File Storage Management", 
category = ComponentCategory.EXTENSION, nonVisible = true, iconName = "images/extension.png")
@UsesLibraries(libraries = "appwrite-android-sdk.aar")
@SimpleObject(external = true)
public class FileStorageManagement extends AndroidNonvisibleComponent {

    private Client client;
    private Storage storage;

    public FileStorageManagement(ComponentContainer container) {
        super(container.$form());
        client = new Client();
        storage = new Storage(client);
    }

    @SimpleFunction(description = "Initialize Appwrite client")
    public void InitializeClient(String endpoint, String projectId, String apiKey) {
        client.setEndpoint(endpoint)
            .setProject(projectId)
            .setKey(apiKey);
    }

    @SimpleFunction(description = "Upload a file to Appwrite storage")
    public void UploadFile(String filePath, String read, String write) {
        storage.createFile(filePath, read, write)
            .addOnSuccessListener(new OnSuccessListener<>() {
                @Override
                public void onSuccess() {
                    // Handle success
                }
            })
            .addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(Exception e) {
                    // Handle error
                }
            });
    }

    @SimpleFunction(description = "Download a file from Appwrite storage")
    public void DownloadFile(String fileId) {
        storage.getFileDownload(fileId)
            .addOnSuccessListener(new OnSuccessListener<>() {
                @Override
                public void onSuccess() {
                    // Handle success
                }
            })
            .addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(Exception e) {
                    // Handle error
                }
            });
    }

    @SimpleFunction(description = "Delete a file from Appwrite storage")
    public void DeleteFile(String fileId) {
        storage.deleteFile(fileId)
            .addOnSuccessListener(new OnSuccessListener<>() {
                @Override
                public void onSuccess() {
                    // Handle success
                }
            })
            .addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(Exception e) {
                    // Handle error
                }
            });
    }
}
```