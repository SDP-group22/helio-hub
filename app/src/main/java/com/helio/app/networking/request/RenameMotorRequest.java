package com.helio.app.networking.request;

/**
 * retrofit serialises these objects to be passed to the Hub for /motor/rename/ requests
 */
@SuppressWarnings({"FieldCanBeLocal", "unused", "RedundantSuppression"})
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
