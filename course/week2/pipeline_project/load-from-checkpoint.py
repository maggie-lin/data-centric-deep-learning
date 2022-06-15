from src.system import DigitClassifierSystem

system = DigitClassifierSystem.load_from_checkpoint(
    './artifacts/ckpts/hparam_flow/width16/epoch=6-step=10500.ckpt')

print(system)
