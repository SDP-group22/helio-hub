package com.helio.app.networking;

import java.util.Map;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

class MotorCallback implements Callback<Motor> {
    protected final Map<Integer, Motor> motors;
    protected final int motorId;

    MotorCallback(Map<Integer, Motor> motors, int motorId) {
        this.motors = motors;
        this.motorId = motorId;
    }

    protected void updateLocalMotorState(Motor m) {
        motors.put(motorId, m);
        System.out.println("Updated local state for " + m);
    }

    protected void unregisterFromLocalMotorState() {
        motors.remove(motorId);
        System.out.println(motorId + " was removed from local state");
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
