package com.helio.app.networking;

import java.util.Map;

import retrofit2.Call;
import retrofit2.Response;

class MotorDeletionCallback extends MotorCallback {

    MotorDeletionCallback(Map<Integer, Motor> motors, int motorId) {
        super(motors, motorId);
    }

    @Override
    public void onResponse(Call<Motor> call, Response<Motor> response) {
        unregisterFromLocalMotorState();
    }
}