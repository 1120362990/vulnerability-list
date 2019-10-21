# -*- coding: utf-8 -*-
import thinkphp.thinkphp5_inj_info
import thinkphp.thinkphp5_x_rce
import thinkphp.thinkphp_before5_0_23_rce


def exec(URL):
    thinkphp.thinkphp5_inj_info.attack(URL)
    thinkphp.thinkphp5_x_rce.attack(URL)
    thinkphp.thinkphp_before5_0_23_rce.attack(URL)


if __name__ == "__main__":
    exec()
