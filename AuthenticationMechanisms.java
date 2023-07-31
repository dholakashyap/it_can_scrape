```java
package com.plus.appzenx;

import io.appwrite.Client;
import io.appwrite.services.Account;

public class AuthenticationMechanisms {

    private Client client;
    private Account account;

    public AuthenticationMechanisms(Client client) {
        this.client = client;
        this.account = new Account(client);
    }

    public void register(String email, String password, String name) {
        try {
            account.create(email, password, name);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void login(String email, String password) {
        try {
            account.createSession(email, password);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void logout() {
        try {
            account.deleteSession("current");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public boolean isAuthenticated() {
        try {
            account.get();
            return true;
        } catch (Exception e) {
            return false;
        }
    }
}
```