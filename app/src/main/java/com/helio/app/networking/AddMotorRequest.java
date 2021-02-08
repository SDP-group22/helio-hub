package com.helio.app.networking;

// helper class, serialized to be used as the body for /motor/register requests
public class AddMotorRequest {
    private int id;
    private String name;
    private String ip;
    private boolean active;

    public AddMotorRequest(int id, String name, String ip, boolean active) {
        this.id = id;
        this.name = name;
        this.ip = ip;
        this.active = active;
    }

    public int getId() {
        return id;
    }
}
