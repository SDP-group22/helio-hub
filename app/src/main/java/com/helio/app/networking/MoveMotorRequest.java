package com.helio.app.networking;

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
