```java
package com.plus.appzenx;

import io.appwrite.Client;
import io.appwrite.services.Functions;

public class CustomFunctions {

    private Client client;
    private Functions functions;

    public CustomFunctions(Client client) {
        this.client = client;
        this.functions = new Functions(client);
    }

    public void createFunction(String name, String runtime) {
        try {
            functions.create(name, runtime).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void listFunctions() {
        try {
            functions.list().get();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void getFunction(String functionId) {
        try {
            functions.get(functionId).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void deleteFunction(String functionId) {
        try {
            functions.delete(functionId).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void executeFunction(String functionId, String payload) {
        try {
            functions.execute(functionId, payload).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```