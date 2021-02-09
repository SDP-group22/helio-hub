package com.helio.app.ui.settings;

import android.os.Bundle;
import android.text.InputType;
import android.widget.PopupWindow;

import androidx.preference.EditTextPreference;
import androidx.preference.ListPreference;
import androidx.preference.Preference;
import androidx.preference.PreferenceFragmentCompat;

import com.helio.app.R;
import com.helio.app.ui.BlindIcon;

public class SingleBlindSettingsFragment extends PreferenceFragmentCompat {
    private PopupWindow changeIconPop;


    @Override
    public void onCreatePreferences(Bundle savedInstanceState, String rootKey) {
        setPreferencesFromResource(R.xml.single_blind_preferences, rootKey);

        EditTextPreference namePreference = findPreference("name");
        EditTextPreference ipPreference = findPreference("ip");
        ListPreference changeIconPreference = findPreference("changeIcon");
        Preference calibrationPreference = findPreference("calibration");
        Preference openNowPreference = findPreference("openNow");
        Preference closeNowPreference = findPreference("closeNow");
        Preference createSchedulePreference = findPreference("createSchedule");
        Preference seeSchedulePreference = findPreference("seeSchedule");
        Preference sensorsPreference = findPreference("sensors");


        //IP
        assert ipPreference != null;
        ipPreference.setOnBindEditTextListener(editText -> editText.setInputType(InputType.TYPE_CLASS_PHONE));


        //Name
        assert namePreference != null;
        namePreference.setOnBindEditTextListener(editText -> editText.setInputType(InputType.TYPE_CLASS_TEXT));

        //change icon


    }
}