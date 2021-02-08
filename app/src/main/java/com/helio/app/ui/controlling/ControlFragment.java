package com.helio.app.ui.controlling;

import androidx.lifecycle.ViewModelProvider;

import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.PopupMenu;
import android.widget.PopupWindow;
import android.widget.TextView;

import com.helio.app.R;

public class ControlFragment extends Fragment {

    private ControlViewModel controlViewModel;

    private EditText IP;
    private EditText name;
    private EditText currentState;
    private Button changeIcon;
    private Button calibration;
    private Button sensors;
    private Button createSchedule;
    private Button save;
    private Button cancel;
    private PopupWindow menu;

    public static ControlFragment newInstance() {
        return new ControlFragment();
    }

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container,
                             @Nullable Bundle savedInstanceState) {
        controlViewModel = new ViewModelProvider(this).get(ControlViewModel.class);
        View returnView = inflater.inflate(R.layout.control_fragment, container, false);

        //map variables to buttons
        IP = returnView.findViewById(R.id.et_IPTextBox);
        name = returnView.findViewById(R.id.et_nameTextBox);
        currentState = returnView.findViewById(R.id.et_currentState);
        changeIcon = returnView.findViewById(R.id.btn_changeIcon);
        calibration = returnView.findViewById(R.id.btn_calibration);
        sensors = returnView.findViewById(R.id.btn_sensors);
        createSchedule = returnView.findViewById(R.id.btn_createSchdule);
        save = returnView.findViewById(R.id.btn_save);
        cancel = returnView.findViewById(R.id.btn_cancel);

        //drop down menu of "change icon"
        changeIcon.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                View view = getLayoutInflater().inflate(R.layout.layout_dropdownmenu,null);
                //when icon is clicked
                TextView tvic1 = view.findViewById(R.id.tv_ic1);
                TextView tvic2 = view.findViewById(R.id.tv_ic2);
                TextView tvic3 = view.findViewById(R.id.tv_ic3);
                TextView tvic4 = view.findViewById(R.id.tv_ic4);
                TextView tvic5 = view.findViewById(R.id.tv_ic5);
                TextView tvic6 = view.findViewById(R.id.tv_ic6);
                TextView tvic7 = view.findViewById(R.id.tv_ic7);
                TextView tvic8 = view.findViewById(R.id.tv_ic8);
                TextView tvic9 = view.findViewById(R.id.tv_ic9);
                TextView tvic10 = view.findViewById(R.id.tv_ic10);
                TextView tvic11 = view.findViewById(R.id.tv_ic11);
                TextView tvic12 = view.findViewById(R.id.tv_ic12);
                TextView tvic13 = view.findViewById(R.id.tv_ic13);
                TextView tvic14 = view.findViewById(R.id.tv_ic14);
//                tvic1.setOnClickListener()
//                tvic2.setOnClickListener();
//                tvic3.setOnClickListener();
//                tvic4.setOnClickListener();
//                tvic5.setOnClickListener();
//                tvic6.setOnClickListener();
//                tvic7.setOnClickListener();
//                tvic8.setOnClickListener();
//                tvic9.setOnClickListener();
//                tvic10.setOnClickListener();
//                tvic11.setOnClickListener();
//                tvic12.setOnClickListener();
//                tvic13.setOnClickListener();
//                tvic14.setOnClickListener();

                menu = new PopupWindow(view,ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT);
                menu.setOutsideTouchable(true);
                menu.setFocusable(true);
                menu.showAsDropDown(changeIcon);
            }
        });


        return returnView;
    }


}