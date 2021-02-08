package com.helio.app.networking;

import java.util.Map;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class HubClient {
    private final HubService service;

    public HubClient(String baseAddress) {
        service = ServiceGenerator.createService(HubService.class, baseAddress);
    }

    public void addMotor(Map<Integer, Motor> motors, AddMotorRequest newMotor) {
        int motorId = newMotor.getId();
        Call<Motor> call = service.addMotor(newMotor);
        call.enqueue(new MotorCallback(motors, motorId));
    }

    public void activateMotor(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.activateMotor(motorId);
        call.enqueue(new MotorCallback(motors, motorId));
    }

    public void getMotor(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.getMotor(motorId);
        call.enqueue(new MotorCallback(motors, motorId));
    }
}

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
