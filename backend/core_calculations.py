import math

def compute_tipping_moment(angle_deg, boom_length=5.0, load_mass=1000.0):
    """ممان واژگونی بر اساس زاویه بوم"""
    g = 9.81
    angle_rad = math.radians(angle_deg)
    horizontal_force = load_mass * g * math.cos(angle_rad)
    return horizontal_force * boom_length

def compute_center_of_gravity(masses_positions):
    """
    محاسبه CG سیستم
    masses_positions: لیست [(mass, position)] به متر
    """
    total_mass = sum(m for m, _ in masses_positions)
    if total_mass == 0:
        return 0
    weighted_sum = sum(m * x for m, x in masses_positions)
    return weighted_sum / total_mass

def compute_axle_loads(cg_position, total_mass, wheelbase, front_axle_offset=0.0):
    """
    محاسبه بار وارد بر هر محور
    cg_position: موقعیت CG نسبت به محور جلو
    wheelbase: فاصله بین محور جلو و عقب
    """
    rear_distance = wheelbase - (cg_position - front_axle_offset)
    front_distance = cg_position - front_axle_offset
    front_load = total_mass * rear_distance / wheelbase
    rear_load = total_mass * front_distance / wheelbase
    return front_load, rear_load

def estimate_swl(boom_angle_deg, boom_length, material_strength=250e6, safety_factor=2.0):
    """
    تخمین ظرفیت بار مجاز (SWL)
    """
    angle_rad = math.radians(boom_angle_deg)
    effective_length = boom_length * math.cos(angle_rad)
    max_force = material_strength / safety_factor
    return max_force * effective_length
