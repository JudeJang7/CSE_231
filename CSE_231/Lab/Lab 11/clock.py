class Time(object):
    
    def __init__( self, hour=0, mins=0, secs=0 ):
        self.__hour = hour
        self.__mins = mins
        self.__secs = secs
        
    def __repr__( self ):
        
        out_str = "Class Time: {:02d}:{:02d}:{:02d}" \
            .format( self.__hour, self.__mins, self.__secs )
            
        return out_str
        
    def __str__( self ):

        out_str = "{:02d}:{:02d}:{:02d}" \
            .format( self.__hour, self.__mins, self.__secs )
            
        return out_str
    
    def from_str( self, out_str ):

        str_list = out_str.replace(":"," ").split()
                    
        self.__hour = int( str_list[0].strip() )
        self.__mins   = int( str_list[1].strip() )
        self.__secs  = int( str_list[2].strip() )