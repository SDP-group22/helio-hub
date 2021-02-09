package com.helio.app.networking;

import java.util.Map;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

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
    public void onResponse(Call<Motor> call, Response<Motor> response) {
        Motor m = response.body();
        if(m != null) {
            System.out.println(call + " succeeded: " + m);
            updateLocalMotorState(m);
        }
    }

    @Override
    public void onFailure(Call<Motor> call, Throwable t) {
        System.out.println(call + " failed: " + t);
    }
}
