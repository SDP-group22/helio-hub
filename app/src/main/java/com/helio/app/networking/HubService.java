package com.helio.app.networking;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.GET;
import retrofit2.http.PATCH;
import retrofit2.http.POST;
import retrofit2.http.Path;

public interface HubService {
    @POST("/motor/register")
    Call<Motor> addMotor(@Body RegisterMotorRequest registerMotorRequest);

    @PATCH("/motor/activate")
    Call<Motor> activateMotor(@Body int motorId);

    @PATCH("/motor/rename")
    Call<Motor> renameMotor(@Body RenameMotorRequest renameMotorRequest);

    @GET("/motor/{motor_id}")
    Call<Motor> getMotor(@Path("motor_id") int motorId);

    @DELETE("/motor/unregister/{motor_id}")
    void deleteMotor(@Path("motor_id") int motorId);
}
