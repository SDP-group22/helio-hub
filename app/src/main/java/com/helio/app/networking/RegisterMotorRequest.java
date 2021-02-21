package com.helio.app.networking;

/**
 * retrofit serialises these objects to be passed to the Hub for /motor/register/ requests
 */
public class RegisterMotorRequest {
    private final boolean active;
    private final int battery;
    private final String ip;
    private final int length;
    private final int level;
    private final String name;
    private final String style;

    public RegisterMotorRequest(String name, String ip, boolean active, int battery, int length, int level, String style) {
        this.name = name;
        this.ip = ip;
        this.active = active;
        this.battery = battery;
        this.length = length;
        this.level = level;
        this.style = style;
    }
}
