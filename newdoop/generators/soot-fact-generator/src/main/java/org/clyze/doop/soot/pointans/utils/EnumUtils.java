package org.clyze.doop.soot.pointans.utils;

import org.clyze.doop.soot.pointans.enums.AdviceEnum;

/**
 * @ClassName   EnumUtils
 * @Description Enumeration of annotations
 */
public class EnumUtils {
    public static AdviceEnum getEnumObject(Object value) {
        for (AdviceEnum adviceEnum : AdviceEnum.values()) {
            if (adviceEnum.getAnnotationClassName().equals(value)) {
                return adviceEnum;
            }
        }
        return null;
    }
}
