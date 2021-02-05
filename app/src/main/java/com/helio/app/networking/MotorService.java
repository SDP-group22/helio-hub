package com.helio.app.networking;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;

public interface MotorService {
    @GET("/motor/{motor_id}")
    public Call<Motor> getMotor(@Path("motor_id") int motorId);
}
