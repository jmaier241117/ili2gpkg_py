package ch.so.agi.ili2gpkg.libnative;

import org.graalvm.nativeimage.IsolateThread;
import org.graalvm.nativeimage.c.function.CEntryPoint;
import org.graalvm.nativeimage.c.type.CCharPointer;
import org.graalvm.nativeimage.c.type.CTypeConversion;
import ch.ehi.ili2gpkg.GpkgMain;

public class Ili2gpkgLib {
    
    @CEntryPoint(name = "ili2gpkg")
    public static boolean convert2GPKG(IsolateThread thread, CCharPointer args) {
            String[] arguments = CTypeConversion.toJavaString(args).split(";");
            GpkgMain.main(arguments);
            return true;
    }

}
