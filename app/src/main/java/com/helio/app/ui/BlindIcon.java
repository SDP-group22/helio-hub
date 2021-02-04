package com.helio.app.ui;

import com.helio.app.R;

/**
 * Represents an icon for identifying blinds (selected by the user)
 */
public enum BlindIcon {
    WINDOW("window", R.drawable.ic_window),
    BEDROOM("bedroom", R.drawable.ic_bed),
    BATHROOM("bathroom", R.drawable.ic_wash),
    KITCHEN("kitchen", R.drawable.ic_fridge),
    SQUARE("square", R.drawable.ic_square),
    STAR("star", R.drawable.ic_star),
    CIRCLE("circle", R.drawable.ic_circle),
    BOOK("book", R.drawable.ic_book),
    CHAIR("chair", R.drawable.ic_chair),
    COMPUTER("computer", R.drawable.ic_computer),
    HOUSE("house", R.drawable.ic_house),
    TV("tv", R.drawable.ic_tv);

    /**
     * Friendly name of the icon
     */
    public final String name;
    /**
     * The id of the resource of the icon
     */
    public final int id;

    BlindIcon(String name, int id) {
        this.name = name;
        this.id = id;
    }

}
