package com.helio.app.networking;

@SuppressWarnings({"FieldCanBeLocal", "unused", "RedundantSuppression"})
public class RenameScheduleRequest {
    private final int id;
    private final String name;

    public RenameScheduleRequest(int id, String name) {
        this.id = id;
        this.name = name;
    }
}
