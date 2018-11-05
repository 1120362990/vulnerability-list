# -*- coding: utf-8 -*-
import os
import fckeditor.fckeditor_version
import fckeditor.fckeditor_dangerfile
import fckeditor.fckeditor_getshell


def exec(URL):
    fckeditor.fckeditor_version.attack(URL)
    fckeditor.fckeditor_dangerfile.attack(URL)
    fckeditor.fckeditor_getshell.attack(URL)




if __name__ == "__main__":
    exec()
