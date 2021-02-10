package com.helio.app.networking;

import com.helio.app.model.Motor;

import org.jetbrains.annotations.NotNull;

import java.util.Map;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

/**
 * A MotorCallback instance allows for code to be run when a response is received from the Hub.
 * It will update our local state to match that of the Hub after performing an action.
 *
 * @see MotorDeletionCallback
 * @see HubClient
 */
class MotorCallback implements Callback<Motor> {
    private final Map<Integer, Motor> motors;
    private final int motorId;

    MotorCallback(Map<Integer, Motor> motors, int motorId) {
        this.motors = motors;
        this.motorId = motorId;
    }

    private void updateLocalMotorState(Motor m) {
        motors.put(motorId, m);
        System.out.println("Updated local state for " + m);
    }

    @Override
    public void onResponse(@NotNull Call<Motor> call, Response<Motor> response) {
        Motor m = response.body();
        if(m != null) {
            System.out.println(call + " succeeded: " + m);
            updateLocalMotorState(m);
        }
    }

    @Override
    public void onFailure(@NotNull Call<Motor> call, @NotNull Throwable t) {
        System.out.println(call + " failed: " + t);
    }
}
