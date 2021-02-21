package com.helio.app.networking;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.helio.app.model.Motor;
import com.helio.app.model.Schedule;

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
                .addConverterFactory(buildCustomConverter())
                .client(httpClient.build());
        Retrofit retrofit = builder.build();
        service = retrofit.create(HubService.class);
    }

    private static GsonConverterFactory buildCustomConverter() {
        GsonBuilder gsonBuilder = new GsonBuilder();

        // Adding custom deserializer
        gsonBuilder.registerTypeAdapter(Schedule.class, new ScheduleDeserializer());
        Gson gson = gsonBuilder.create();

        return GsonConverterFactory.create(gson);
    }

    public void addMotor(Map<Integer, Motor> motors, RegisterMotorRequest registerMotorRequest) {
        Call<Motor> call = service.addMotor(registerMotorRequest);
        call.enqueue(new MyCallback<>(motors));
    }

    public void activateMotor(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.activateMotor(motorId);
        call.enqueue(new MyCallback<>(motors));
    }

    public void deactivateMotor(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.deactivateMotor(motorId);
        call.enqueue(new MyCallback<>(motors));
    }

    public void renameMotor(Map<Integer, Motor> motors, RenameMotorRequest renameMotorRequest) {
        Call<Motor> call = service.renameMotor(renameMotorRequest);
        call.enqueue(new MyCallback<>(motors));
    }

    public void getMotor(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.getMotor(motorId);
        call.enqueue(new MyCallback<>(motors));
    }

    public void moveMotor(Map<Integer, Motor> motors, MoveMotorRequest moveMotorRequest) {
        Call<Motor> call = service.moveMotor(moveMotorRequest);
        call.enqueue(new MyCallback<>(motors));
    }

    public void startMotorCalibration(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.startMotorCalibration(motorId);
        call.enqueue(new MyCallback<>(motors));
    }

    public void stopMotorCalibration(Map<Integer, Motor> motors, int motorId) {
        Call<Motor> call = service.stopMotorCalibration(motorId);
        call.enqueue(new MyCallback<>(motors));
    }

    public void deleteMotor(Map<Integer, Motor> motors, int motorId) {
        Call<ResponseBody> call = service.deleteMotor(motorId);
        call.enqueue(new MyDeletionCallback<>(motors, motorId));
    }

    public void addSchedule(Map<Integer, Schedule> schedules, RegisterScheduleRequest registerScheduleRequest) {
        Call<Schedule> call = service.addSchedule(registerScheduleRequest);
        call.enqueue(new MyCallback<>(schedules));
    }

    public void deleteSchedule(Map<Integer, Schedule> schedules, int id) {
        Call<ResponseBody> call = service.deleteSchedule(id);
        call.enqueue(new MyDeletionCallback<>(schedules, id));
    }

    public void changeDaysSchedule(Map<Integer, Schedule> schedules, ChangeDaysScheduleRequest changeDaysScheduleRequest) {
        Call<Schedule> call = service.changeDaysSchedule(changeDaysScheduleRequest);
        call.enqueue(new MyCallback<>(schedules));
    }

    public void changeTimeSchedule(Map<Integer, Schedule> schedules, ChangeTimeScheduleRequest changeTimeScheduleRequest) {
        Call<Schedule> call = service.changeTimeSchedule(changeTimeScheduleRequest);
        call.enqueue(new MyCallback<>(schedules));
    }

    public void changeGradientSchedule(Map<Integer, Schedule> schedules, ChangeGradientScheduleRequest changeGradientScheduleRequest) {
        Call<Schedule> call = service.changeGradientSchedule(changeGradientScheduleRequest);
        call.enqueue(new MyCallback<>(schedules));
    }

    public void renameSchedule(Map<Integer, Schedule> schedules, RenameScheduleRequest renameScheduleRequest) {
        Call<Schedule> call = service.renameSchedule(renameScheduleRequest);
        call.enqueue(new MyCallback<>(schedules));
    }

    public void activateSchedule(Map<Integer, Schedule> schedules, int id) {
        Call<Schedule> call = service.activateSchedule(id);
        call.enqueue(new MyCallback<>(schedules));
    }

    public void deactivateSchedule(Map<Integer, Schedule> schedules, int id) {
        Call<Schedule> call = service.deactivateSchedule(id);
        call.enqueue(new MyCallback<>(schedules));
    }
}
