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

    public void addMotor(Map<Integer, Motor> motors, RegisterMotorRequest registerMotorRequest) {
        int motorId = registerMotorRequest.getId();
        Call<Motor> call = service.addMotor(registerMotorRequest);
        call.enqueue(new MotorCallback(motors, motorId));
    }

    public void activateMotor(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.activateMotor(motorId);
        call.enqueue(new MotorCallback(motors, motorId));
    }

    public void deactivateMotor(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.deactivateMotor(motorId);
        call.enqueue(new MotorCallback(motors, motorId));
    }

    public void renameMotor(Map<Integer, Motor> motors, RenameMotorRequest renameMotorRequest) {
        int motorId = renameMotorRequest.getId();
        Call<Motor> call = service.renameMotor(renameMotorRequest);
        call.enqueue(new MotorCallback(motors, motorId));
    }

    public void getMotor(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.getMotor(motorId);
        call.enqueue(new MotorCallback(motors, motorId));
    }

    public void moveMotor(Map<Integer, Motor> motors, MoveMotorRequest moveMotorRequest) {
        int motorId = moveMotorRequest.getId();
        Call<Motor> call = service.moveMotor(moveMotorRequest);
        call.enqueue(new MotorCallback(motors, motorId));
    }

    public void startMotorCalibration(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.startMotorCalibration(motorId);
        call.enqueue(new MotorCallback(motors, motorId));
    }

    public void stopMotorCalibration(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.stopMotorCalibration(motorId);
        call.enqueue(new MotorCallback(motors, motorId));
    }

    public void deleteMotor(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.deleteMotor(motorId);
        call.enqueue(new MotorDeletionCallback(motors, motorId));
    }
}
