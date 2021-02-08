package com.helio.app.networking;

public class RenameMotorRequest {
    private final int id;
    private final String newName;

    public RenameMotorRequest(int id, String newName) {
        this.id = id;
        this.newName = newName;
    }

    public int getId() {
        return id;
    }
}
