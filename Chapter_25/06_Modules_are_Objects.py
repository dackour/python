# Example: Modules Are Objects
import alls
alls.a  # Qualify object by attribute
alls.__dict__['a']  # Index namespace dictionary manually
sys.modules['alls'].a  # Index loaded-modules table manually
getattr(alls, 'a')  # Call built-in fetch function