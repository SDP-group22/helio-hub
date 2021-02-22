package com.helio.app.networking.request;

import com.google.gson.annotations.SerializedName;

import java.util.List;

@SuppressWarnings({"FieldCanBeLocal", "unused", "RedundantSuppression"})
public abstract class RegisterMotionSensorRequest extends RegisterSensorRequest {
    @SerializedName("duration_sensitivity")
    private final int durationSensitivity;

    public RegisterMotionSensorRequest(List<Integer> motorIds, String name, String ip, boolean active, int battery, String style, int durationSensitivity) {
        super(motorIds, name, ip, active, battery, style);
        this.durationSensitivity = durationSensitivity;
    }
}
