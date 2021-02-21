package com.helio.app.networking;

import com.helio.app.model.Motor;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.GET;
import retrofit2.http.PATCH;
import retrofit2.http.POST;
import retrofit2.http.Path;

/**
 * This interface matches the OpenAPI specification we came up with as a group.
 *
 * @see HubClient
 */
public interface HubService {
    @POST("/motor/register")
    Call<Motor> addMotor(@Body RegisterMotorRequest registerMotorRequest);

    @PATCH("/motor/activate/{motor_id}")
    Call<Motor> activateMotor(@Path("motor_id") int motorId);

    @PATCH("/motor/deactivate/{motor_id}")
    Call<Motor> deactivateMotor(@Path("motor_id") int motorId);

    @PATCH("/motor/rename")
    Call<Motor> renameMotor(@Body RenameMotorRequest renameMotorRequest);

    @GET("/motor/{motor_id}")
    Call<Motor> getMotor(@Path("motor_id") int motorId);

    @PATCH("/motor/move")
    Call<Motor> moveMotor(@Body MoveMotorRequest moveMotorRequest);

    @PATCH("/motor/start_calibrate/{motor_id}")
    Call<Motor> startMotorCalibration(@Path("motor_id") int motorId);

    @PATCH("/motor/stop_calibrate/{motor_id}")
    Call<Motor> stopMotorCalibration(@Path("motor_id") int motorId);

    @DELETE("/motor/unregister/{motor_id}")
    Call<ResponseBody> deleteMotor(@Path("motor_id") int motorId);
}
