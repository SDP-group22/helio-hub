package com.helio.app.networking;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.GET;
import retrofit2.http.PATCH;
import retrofit2.http.POST;
import retrofit2.http.Path;
import retrofit2.http.Query;

public interface HubService {
    @POST("/motor/register")
    Call<Motor> addMotor(@Body AddMotorRequest newMotorParameters);

    @PATCH("/motor/activate")
    Call<Motor> activateMotor(@Body int motorId);

    @GET("/motor/{motor_id}")
    Call<Motor> getMotor(@Path("motor_id") int motorId);

    @DELETE("/motor/unregister/{motor_id}")
    void deleteMotor(@Path("motor_id") int motorId);
}
