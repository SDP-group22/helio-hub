package com.helio.app.networking;

/**
 * retrofit serialises these objects to be passed to the Hub for /motor/register/ requests
 */
public class RegisterMotorRequest {
    private final int id;
    private final String name;
    private final String ip;
    private final boolean active;

    public RegisterMotorRequest(int id, String name, String ip, boolean active) {
        this.id = id;
        this.name = name;
        this.ip = ip;
        this.active = active;
    }

    public int getId() {
        return id;
    }
}
