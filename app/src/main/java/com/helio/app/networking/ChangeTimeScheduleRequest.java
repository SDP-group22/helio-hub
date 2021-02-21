package com.helio.app.networking;

@SuppressWarnings({"FieldCanBeLocal", "unused", "RedundantSuppression"})
public class ChangeTimeScheduleRequest {
    private final int id;
    private final String time;

    public ChangeTimeScheduleRequest(int id, String time) {
        this.id = id;
        this.time = time;
    }
}
