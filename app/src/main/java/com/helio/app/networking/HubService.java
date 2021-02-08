package com.helio.app.networking;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.DELETE;
import retrofit2.http.GET;
import retrofit2.http.Path;

public interface HubService {
    @GET("/motor/{motor_id}")
    public Call<Motor> getMotor(@Path("motor_id") int motorId);

    @GET("/motor/get_all")
    public Call<List<Motor>> getMotors();

    @DELETE("/motor/unregister/{motor_id}")
    public void deleteMotor(@Path("motor_id") int motorId);
}
