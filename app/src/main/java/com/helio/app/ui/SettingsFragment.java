package com.helio.app.ui;

import android.os.Bundle;
import android.text.InputType;
import android.widget.EditText;

import androidx.annotation.NonNull;
import androidx.preference.DropDownPreference;
import androidx.preference.EditTextPreference;
import androidx.preference.Preference;
import androidx.preference.PreferenceFragmentCompat;

import com.helio.app.R;

public class SettingsFragment extends PreferenceFragmentCompat {

    @Override
    public void onCreatePreferences(Bundle savedInstanceState, String rootKey) {
        setPreferencesFromResource(R.xml.preferences, rootKey);

        EditTextPreference namePreference = findPreference("name");
        EditTextPreference ipPreference = findPreference("ip");
        DropDownPreference changeIconPreference = findPreference("changeIcon");
        Preference calibrationPreference = findPreference("calibration");
        Preference openNowPreference = findPreference("openNow");
        Preference closeNowPreference = findPreference("closeNow");
        Preference createSchedulePreference = findPreference("createSchedule");
        Preference seeSchedulePreference = findPreference("seeSchedule");
        Preference sensorsPreference = findPreference("sensors");

        //IP
        if (ipPreference != null) {
            ipPreference.setOnBindEditTextListener(new EditTextPreference.OnBindEditTextListener() {
                        @Override
                        public void onBindEditText(@NonNull EditText editText) {
                            editText.setInputType(InputType.TYPE_CLASS_NUMBER);
                        }
                    });
        }

        //Name
        if (namePreference != null) {
            namePreference.setOnBindEditTextListener(new EditTextPreference.OnBindEditTextListener() {
                @Override
                public void onBindEditText(@NonNull EditText editText) {
                    editText.setInputType(InputType.TYPE_CLASS_TEXT);
                }
            });
        }






    }
}