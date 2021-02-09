package com.helio.app.networking;

import org.jetbrains.annotations.NotNull;

import java.util.Map;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

/**
 * A MotorDeletionCallback instance allows for code to be run after deleting a motor on the Hub.
 * To remain in sync with the Hub, we also remove that motor from our local state.
 *
 * @see MotorCallback
 * @see HubClient
 */
class MotorDeletionCallback implements Callback<ResponseBody> {
    private final Map<Integer, Motor> motors;
    private final int motorId;

    MotorDeletionCallback(Map<Integer, Motor> motors, int motorId) {
        this.motors = motors;
        this.motorId = motorId;
    }

    private void unregisterFromLocalMotorState() {
        motors.remove(motorId);
        System.out.println(motorId + " was removed from local state");
    }

    @Override
    public void onResponse(
            @NotNull Call<ResponseBody> call,
            @NotNull Response<ResponseBody> response
    ) {
        unregisterFromLocalMotorState();
    }

    @Override
    public void onFailure(@NotNull Call<ResponseBody> call, @NotNull Throwable t) {
        System.out.println(call + " failed: " + t);
    }
}