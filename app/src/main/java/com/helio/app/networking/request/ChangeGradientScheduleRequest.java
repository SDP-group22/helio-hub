package com.helio.app.networking.request;

@SuppressWarnings({"FieldCanBeLocal", "unused", "RedundantSuppression"})
public class ChangeGradientScheduleRequest {
    private final int id;
    private final int gradient;

    public ChangeGradientScheduleRequest(int id, int gradient) {
        this.id = id;
        this.gradient = gradient;
    }
}
