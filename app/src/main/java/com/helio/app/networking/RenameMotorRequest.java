package com.helio.app.networking;

public class RenameMotorRequest {
    private final int id;
    private final String name;

    public RenameMotorRequest(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() {
        return id;
    }
}
