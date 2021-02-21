package com.helio.app.networking;

import com.helio.app.model.Motor;

import java.util.Map;

import okhttp3.OkHttpClient;
import okhttp3.ResponseBody;
import okhttp3.logging.HttpLoggingInterceptor;
import retrofit2.Call;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;


/**
 * HubClient is the client-side code we use to communicate with the Hub.
 * Using retrofit and an interface that matches our OpenAPI specification, sending requests becomes
 * quite easy to do.<br/>
 * The following methods abstract this away further, by automatically updating our local state after
 * we receive a response.
 *
 * @see HubService
 */
public class HubClient {
    private final HubService service;

    public HubClient(String baseAddress) {
        // Logging: https://stackoverflow.com/a/33328524/
        HttpLoggingInterceptor logging = new HttpLoggingInterceptor();
        logging.setLevel(HttpLoggingInterceptor.Level.BODY); // Logging level
        OkHttpClient.Builder httpClient = new OkHttpClient.Builder();
        httpClient.addInterceptor(logging);

        Retrofit.Builder builder = new Retrofit.Builder()
                .baseUrl(baseAddress)
                .addConverterFactory(GsonConverterFactory.create())
                .client(httpClient.build());
        Retrofit retrofit = builder.build();
        service = retrofit.create(HubService.class);
    }

    public void addMotor(Map<Integer, Motor> motors, RegisterMotorRequest registerMotorRequest) {
        Call<Motor> call = service.addMotor(registerMotorRequest);
        System.out.println(call.toString());
        call.enqueue(new MotorCallback(motors));
    }

    public void activateMotor(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.activateMotor(motorId);
        call.enqueue(new MotorCallback(motors));
    }

    public void deactivateMotor(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.deactivateMotor(motorId);
        call.enqueue(new MotorCallback(motors));
    }

    public void renameMotor(Map<Integer, Motor> motors, RenameMotorRequest renameMotorRequest) {
        Call<Motor> call = service.renameMotor(renameMotorRequest);
        call.enqueue(new MotorCallback(motors));
    }

    public void getMotor(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.getMotor(motorId);
        call.enqueue(new MotorCallback(motors));
    }

    public void moveMotor(Map<Integer, Motor> motors, MoveMotorRequest moveMotorRequest) {
        Call<Motor> call = service.moveMotor(moveMotorRequest);
        call.enqueue(new MotorCallback(motors));
    }

    public void startMotorCalibration(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.startMotorCalibration(motorId);
        call.enqueue(new MotorCallback(motors));
    }

    public void stopMotorCalibration(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.stopMotorCalibration(motorId);
        call.enqueue(new MotorCallback(motors));
    }

    public void deleteMotor(Map<Integer, Motor> motors, int motorId) {
        Call<ResponseBody> call = service.deleteMotor(motorId);
        call.enqueue(new MotorDeletionCallback(motors, motorId));
    }
}
