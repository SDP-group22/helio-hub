package com.helio.app.networking;

/**
 * retrofit serialises these objects to be passed to the Hub for /motor/move/ requests
 */
public class MoveMotorRequest {
    private final int id;
    private final int level;

    public MoveMotorRequest(int id, int level) {
        this.id = id;
        this.level = level;
    }

    public int getId() {
        return id;
    }
}
