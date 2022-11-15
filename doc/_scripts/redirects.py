"""
Copyright (c) 2021 Zephyr Project members and individual contributors
SPDX-License-Identifier: Apache-2.0

This module contains a variable with a list of tuples (old_url, new_url) for
pages to redirect. This list allows redirecting old URLs (caused by reorganizing
doc directories)

Notes:
    - Please keep this list sorted alphabetically.
    - URLs must be relative to document root (with NO leading slash), and
      without the html extension).
"""

REDIRECTS = [
    ("api/api", "reference/index"),
    ("api/index", "reference/index"),
    ("application/application", "application/index.rst"),
    ("boards/arc/em_starterkit/doc/board", "boards/arc/em_starterkit/doc/index"),
    ("boards/arc/nsim_em/doc/board", "boards/arc/nsim_em/doc/index"),
    ("boards/arm/96b_argonkey/doc/96b_argonkey", "boards/arm/96b_argonkey/doc/index"),
    ("boards/arm/96b_carbon/doc/96b_carbon", "boards/arm/96b_carbon/doc/index"),
    (
        "boards/arm/96b_carbon_nrf51/doc/96b_carbon_nrf51",
        "boards/arm/96b_carbon_nrf51/doc/index",
    ),
    ("boards/arm/96b_neonkey/doc/96b_neonkey", "boards/arm/96b_neonkey/doc/index"),
    ("boards/arm/96b_nitrogen/doc/96b_nitrogen", "boards/arm/96b_nitrogen/doc/index"),
    (
        "boards/arm/adafruit_feather_m0_basic_proto/doc/adafruit_feather_m0_basic_proto",
        "boards/arm/adafruit_feather_m0_basic_proto/doc/index",
    ),
    (
        "boards/arm/adafruit_trinket_m0/doc/adafruit_trinket_m0",
        "boards/arm/adafruit_trinket_m0/doc/index",
    ),
    ("boards/arm/arduino_due/doc/board", "boards/arm/arduino_due/doc/index"),
    ("boards/arm/arduino_zero/doc/arduino_zero", "boards/arm/arduino_zero/doc/index"),
    (
        "boards/arm/atsamd20_xpro/doc/atsamd20_xpro",
        "boards/arm/atsamd20_xpro/doc/index",
    ),
    ("boards/arm/bbc_microbit/doc/board", "boards/arm/bbc_microbit/doc/index"),
    (
        "boards/arm/cc3220sf_launchxl/doc/cc3220sf_launchxl",
        "boards/arm/cc3220sf_launchxl/doc/index",
    ),
    (
        "boards/arm/colibri_imx7d_m4/doc/colibri_imx7d_m4",
        "boards/arm/colibri_imx7d_m4/doc/index",
    ),
    (
        "boards/arm/disco_l475_iot1/doc/disco_l475_iot1",
        "boards/arm/disco_l475_iot1/doc/index",
    ),
    (
        "boards/arm/dragino_lsn50/doc/dragino_lsn50",
        "boards/arm/dragino_lsn50/doc/index",
    ),
    (
        "boards/arm/efm32wg_stk3800/doc/efm32wg_stk3800",
        "boards/arm/efm32wg_stk3800/doc/index",
    ),
    (
        "boards/arm/efr32_slwstk6061a/doc/efr32_slwstk6061a",
        "boards/arm/efr32_slwstk6061a/doc/index",
    ),
    ("boards/arm/frdm_k64f/doc/frdm_k64f", "boards/arm/frdm_k64f/doc/index"),
    ("boards/arm/frdm_kl25z/doc/frdm_kl25z", "boards/arm/frdm_kl25z/doc/index"),
    ("boards/arm/frdm_kw41z/doc/frdm_kw41z", "boards/arm/frdm_kw41z/doc/index"),
    ("boards/arm/hexiwear_k64/doc/hexiwear_k64", "boards/arm/hexiwear_k64/doc/index"),
    (
        "boards/arm/hexiwear_kw40z/doc/hexiwear_kw40z",
        "boards/arm/hexiwear_kw40z/doc/index",
    ),
    (
        "boards/arm/lpcxpresso54114_m0/doc/lpcxpresso54114_m0",
        "boards/arm/lpcxpresso54114_m0/doc/index",
    ),
    (
        "boards/arm/lpcxpresso54114_m4/doc/lpcxpresso54114",
        "boards/arm/lpcxpresso54114_m4/doc/index",
    ),
    (
        "boards/arm/mimxrt1020_evk/doc/mimxrt1020_evk",
        "boards/arm/mimxrt1020_evk/doc/index",
    ),
    (
        "boards/arm/mimxrt1050_evk/doc/mimxrt1050_evk",
        "boards/arm/mimxrt1050_evk/doc/index",
    ),
    (
        "boards/arm/mimxrt1060_evk/doc/mimxrt1060_evk",
        "boards/arm/mimxrt1060_evk/doc/index",
    ),
    (
        "boards/arm/mimxrt1064_evk/doc/mimxrt1064_evk",
        "boards/arm/mimxrt1064_evk/doc/index",
    ),
    ("boards/arm/mps2_an385/doc/mps2_an385", "boards/arm/mps2_an385/doc/index"),
    (
        "boards/arm/msp_exp432p401r_launchxl/doc/msp_exp432p401r_launchxl",
        "boards/arm/msp_exp432p401r_launchxl/doc/index",
    ),
    ("boards/arm/nrf51_ble400/doc/nrf51_ble400", "boards/arm/nrf51_ble400/doc/index"),
    (
        "boards/arm/nrf51_blenano/doc/nrf51_blenano",
        "boards/arm/nrf51_blenano/doc/index",
    ),
    ("boards/arm/nrf51_pca10028/doc/index", "boards/arm/nrf51dk_nrf51422/doc/index"),
    (
        "boards/arm/nrf51_pca10028/doc/nrf51_pca10028",
        "boards/arm/nrf51dk_nrf51422/doc/index",
    ),
    (
        "boards/arm/nrf51_pca10031/doc/index",
        "boards/arm/nrf51dongle_nrf51422/doc/index",
    ),
    (
        "boards/arm/nrf51_vbluno51/doc/nrf51_vbluno51",
        "boards/arm/nrf51_vbluno51/doc/index",
    ),
    ("boards/arm/nrf52810_pca10040/doc/index", "boards/arm/nrf52dk_nrf52810/doc/index"),
    (
        "boards/arm/nrf52810_pca10040/doc/nrf52810_pca10040",
        "boards/arm/nrf52dk_nrf52810/doc/index",
    ),
    (
        "boards/arm/nrf52811_pca10056/doc/index",
        "boards/arm/nrf52840dk_nrf52811/doc/index",
    ),
    (
        "boards/arm/nrf52833_pca10100/doc/index",
        "boards/arm/nrf52833dk_nrf52833/doc/index",
    ),
    (
        "boards/arm/nrf52840_pca10056/doc/index",
        "boards/arm/nrf52840dk_nrf52840/doc/index",
    ),
    (
        "boards/arm/nrf52840_pca10056/doc/nrf52840_pca10056",
        "boards/arm/nrf52840dk_nrf52840/doc/index",
    ),
    (
        "boards/arm/nrf52840_pca10059/doc/index",
        "boards/arm/nrf52840dongle_nrf52840/doc/index",
    ),
    (
        "boards/arm/nrf52840_pca10059/doc/nrf52840_pca10059",
        "boards/arm/nrf52840dongle_nrf52840/doc/index",
    ),
    (
        "boards/arm/nrf52840_pca10090/doc/index",
        "boards/arm/nrf9160dk_nrf52840/doc/index",
    ),
    (
        "boards/arm/nrf52_adafruit_feather/doc/nrf52_adafruit_feather",
        "boards/arm/nrf52_adafruit_feather/doc/index",
    ),
    (
        "boards/arm/nrf52_blenano2/doc/nrf52_blenano2",
        "boards/arm/nrf52_blenano2/doc/index",
    ),
    ("boards/arm/nrf52_pca10040/doc/index", "boards/arm/nrf52dk_nrf52832/doc/index"),
    (
        "boards/arm/nrf52_pca10040/doc/nrf52_pca10040",
        "boards/arm/nrf52dk_nrf52832/doc/index",
    ),
    ("boards/arm/nrf52_pca20020/doc/index", "boards/arm/thingy52_nrf52832/doc/index"),
    (
        "boards/arm/nrf52_pca20020/doc/nrf52_pca20020",
        "boards/arm/thingy52_nrf52832/doc/index",
    ),
    (
        "boards/arm/nrf52_vbluno52/doc/nrf52_vbluno52",
        "boards/arm/nrf52_vbluno52/doc/index",
    ),
    (
        "boards/arm/nrf5340_dk_nrf5340/doc/index",
        "boards/arm/nrf5340pdk_nrf5340/doc/index",
    ),
    ("boards/arm/nrf9160_pca10090/doc/index", "boards/arm/nrf9160dk_nrf9160/doc/index"),
    ("boards/arm/nucleo_f030r8/doc/nucleof030r8", "boards/arm/nucleo_f030r8/doc/index"),
    ("boards/arm/nucleo_f070rb/doc/nucleof070rb", "boards/arm/nucleo_f070rb/doc/index"),
    ("boards/arm/nucleo_f091rc/doc/nucleof091rc", "boards/arm/nucleo_f091rc/doc/index"),
    ("boards/arm/nucleo_f103rb/doc/nucleof103rb", "boards/arm/nucleo_f103rb/doc/index"),
    (
        "boards/arm/nucleo_f207zg/doc/nucleo_f207zg",
        "boards/arm/nucleo_f207zg/doc/index",
    ),
    ("boards/arm/nucleo_f334r8/doc/nucleof334r8", "boards/arm/nucleo_f334r8/doc/index"),
    ("boards/arm/nucleo_f401re/doc/nucleof401re", "boards/arm/nucleo_f401re/doc/index"),
    ("boards/arm/nucleo_f411re/doc/nucleof411re", "boards/arm/nucleo_f411re/doc/index"),
    ("boards/arm/nucleo_f412zg/doc/nucleof412zg", "boards/arm/nucleo_f412zg/doc/index"),
    ("boards/arm/nucleo_f413zh/doc/nucleof413zh", "boards/arm/nucleo_f413zh/doc/index"),
    ("boards/arm/nucleo_f429zi/doc/nucleof429zi", "boards/arm/nucleo_f429zi/doc/index"),
    ("boards/arm/nucleo_f446re/doc/nucleof446re", "boards/arm/nucleo_f446re/doc/index"),
    ("boards/arm/nucleo_l053r8/doc/nucleol053r8", "boards/arm/nucleo_l053r8/doc/index"),
    ("boards/arm/nucleo_l073rz/doc/nucleol073rz", "boards/arm/nucleo_l073rz/doc/index"),
    ("boards/arm/nucleo_l432kc/doc/nucleol432kc", "boards/arm/nucleo_l432kc/doc/index"),
    ("boards/arm/nucleo_l476rg/doc/nucleol476rg", "boards/arm/nucleo_l476rg/doc/index"),
    (
        "boards/arm/olimex_stm32_e407/doc/olimex_stm32_e407",
        "boards/arm/olimex_stm32_e407/doc/index",
    ),
    (
        "boards/arm/olimex_stm32_h407/doc/olimex_stm32_h407",
        "boards/arm/olimex_stm32_h407/doc/index",
    ),
    (
        "boards/arm/olimex_stm32_p405/doc/olimex_stm32_p405",
        "boards/arm/olimex_stm32_p405/doc/index",
    ),
    (
        "boards/arm/olimexino_stm32/doc/olimexino_stm32",
        "boards/arm/olimexino_stm32/doc/index",
    ),
    ("boards/arm/qemu_cortex_m3/doc/board", "boards/arm/qemu_cortex_m3/doc/index"),
    ("boards/arm/reel_board/doc/reel_board", "boards/arm/reel_board/doc/index"),
    (
        "boards/arm/sam4s_xplained/doc/sam4s_xplained",
        "boards/arm/sam4s_xplained/doc/index",
    ),
    (
        "boards/arm/sam_e70_xplained/doc/sam_e70_xplained",
        "boards/arm/sam_e70_xplained/doc/index",
    ),
    (
        "boards/arm/stm3210c_eval/doc/stm3210c_eval",
        "boards/arm/stm3210c_eval/doc/index",
    ),
    (
        "boards/arm/stm32373c_eval/doc/stm32373c_eval",
        "boards/arm/stm32373c_eval/doc/index",
    ),
    (
        "boards/arm/stm32_min_dev/doc/stm32_min_dev",
        "boards/arm/stm32_min_dev/doc/index",
    ),
    (
        "boards/arm/stm32f072_eval/doc/stm32f072_eval",
        "boards/arm/stm32f072_eval/doc/index",
    ),
    (
        "boards/arm/stm32f072b_disco/doc/stm32f072b_disco",
        "boards/arm/stm32f072b_disco/doc/index",
    ),
    (
        "boards/arm/stm32f0_disco/doc/stm32f0_disco",
        "boards/arm/stm32f0_disco/doc/index",
    ),
    (
        "boards/arm/stm32f3_disco/doc/stm32f3_disco",
        "boards/arm/stm32f3_disco/doc/index",
    ),
    (
        "boards/arm/stm32f411e_disco/doc/stm32f411e_disco",
        "boards/arm/stm32f411e_disco/doc/index",
    ),
    (
        "boards/arm/stm32f412g_disco/doc/stm32f412g_disco",
        "boards/arm/stm32f412g_disco/doc/index",
    ),
    (
        "boards/arm/stm32f429i_disc1/doc/stm32f429i_disc1",
        "boards/arm/stm32f429i_disc1/doc/index",
    ),
    (
        "boards/arm/stm32f469i_disco/doc/stm32f469i_disco",
        "boards/arm/stm32f469i_disco/doc/index",
    ),
    (
        "boards/arm/stm32f4_disco/doc/stm32f4_disco",
        "boards/arm/stm32f4_disco/doc/index",
    ),
    (
        "boards/arm/stm32f723e_disco/doc/stm32f723e_disco",
        "boards/arm/stm32f723e_disco/doc/index",
    ),
    (
        "boards/arm/stm32f746g_disco/doc/stm32f746g_disco",
        "boards/arm/stm32f746g_disco/doc/index",
    ),
    (
        "boards/arm/stm32f769i_disco/doc/stm32f769i_disco",
        "boards/arm/stm32f769i_disco/doc/index",
    ),
    (
        "boards/arm/stm32l476g_disco/doc/stm32l476g_disco",
        "boards/arm/stm32l476g_disco/doc/index",
    ),
    (
        "boards/arm/stm32l496g_disco/doc/stm32l496g_disco",
        "boards/arm/stm32l496g_disco/doc/index",
    ),
    (
        "boards/arm/udoo_neo_full_m4/doc/udoo_neo_full",
        "boards/arm/udoo_neo_full_m4/doc/index",
    ),
    ("boards/arm/usb_kw24d512/doc/usb_kw24d512", "boards/arm/usb_kw24d512/doc/index"),
    ("boards/arm/v2m_beetle/doc/v2m_beetle", "boards/arm/v2m_beetle/doc/index"),
    ("boards/arm/warp7_m4/doc/warp7_m4", "boards/arm/warp7_m4/doc/index"),
    ("boards/boards", "boards/index"),
    ("boards/nios2/altera_max10/doc/board", "boards/nios2/altera_max10/doc/index"),
    ("boards/nios2/qemu_nios2/doc/board", "boards/nios2/qemu_nios2/doc/index"),
    ("boards/posix/native_posix/doc/board", "boards/posix/native_posix/doc/index"),
    ("boards/riscv/hifive1/doc/hifive1", "boards/riscv/hifive1/doc/index"),
    ("boards/riscv/hifive1/doc/index", "boards/riscv/hifive1/doc/index"),
    ("boards/riscv/hifive1_revb/doc/index", "boards/riscv/hifive1_revb/doc/index"),
    (
        "boards/riscv/litex_vexriscv/doc/litex_vexriscv",
        "boards/riscv/litex_vexriscv/doc/litex_vexriscv",
    ),
    ("boards/riscv/m2gl025_miv/doc/index", "boards/riscv/m2gl025_miv/doc/index"),
    ("boards/riscv/m2gl025_miv/doc/m2g1025_miv", "boards/riscv/m2gl025_miv/doc/index"),
    ("boards/riscv/qemu_riscv32/doc/board", "boards/riscv/qemu_riscv32/doc/index"),
    ("boards/riscv/qemu_riscv32/doc/index", "boards/riscv/qemu_riscv32/doc/index"),
    ("boards/riscv/rv32m1_vega/doc/index", "boards/riscv/rv32m1_vega/doc/index"),
    (
        "boards/riscv/zedboard_pulpino/doc/zedboard_pulpino",
        "boards/riscv/zedboard_pulpino/doc/index",
    ),
    ("boards/x86/arduino_101/doc/board", "boards/x86/arduino_101/doc/index"),
    ("boards/x86/galileo/doc/galileo", "boards/x86/galileo/doc/index"),
    ("boards/x86/qemu_x86/doc/board", "boards/x86/qemu_x86/doc/index"),
    ("boards/x86/tinytile/doc/board", "boards/x86/tinytile/doc/index"),
    ("boards/x86/up_squared/doc/up_squared", "boards/x86/up_squared/doc/index"),
    ("boards/x86/x86_jailhouse/doc/board", "boards/x86/x86_jailhouse/doc/index"),
    ("boards/xtensa/esp32/doc/esp32", "boards/xtensa/esp32/doc/index"),
    (
        "boards/xtensa/intel_s1000_crb/doc/intel_s1000",
        "boards/xtensa/intel_s1000_crb/doc/index",
    ),
    ("boards/xtensa/qemu_xtensa/doc/board", "boards/xtensa/qemu_xtensa/doc/index"),
    ("boards/xtensa/xt-sim/doc/xt-sim", "boards/xtensa/xt-sim/doc/index"),
    ("contribute/contribute_guidelines", "contribute/index"),
    ("getting_started/getting_started", "getting_started/index"),
    ("guides/debugging/coredump", "guides/flash_debug/coredump"),
    ("guides/debugging/gdbstub", "guides/flash_debug/gdbstub"),
    ("guides/debugging/host-tools", "guides/flash_debug/host-tools"),
    ("guides/debugging/index", "guides/flash_debug/index"),
    ("guides/debugging/probes", "guides/flash_debug/probes"),
    ("guides/debugging/thread-analyzer", "guides/flash_debug/thread-analyzer"),
    ("guides/c_library", "reference/libc/index"),
    ("guides/west/repo-tool", "guides/west/basics"),
    ("introduction/introducing_zephyr", "introduction/index"),
    ("kernel/kernel", "reference/kernel/index"),
    ("releases/release-notes", "releases/index"),
    ("samples/samples", "samples/index"),
    ("security/security", "security/index"),
    ("subsystems/subsystems", "reference/index"),
]
