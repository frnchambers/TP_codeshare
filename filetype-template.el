;; Autoload filetype templates - Doesn't seem to work for more than one filetype, syntax?
(auto-insert-mode)  ;;; Adds hook to find-files-hook
    (setq auto-insert-directory "/home/ruairi/.emacs.d/autoinsert/") ;;; Path to templates, *NOTE* Trailing slash important
    (setq auto-insert-query nil) ;;; If you don't want to be prompted before insertion
    (define-auto-insert "\.tex" "template.tex")
    ;; (define-auto-insert "\.h" "template.h")
    ;; (define-auto-insert "\.cpp" "template.cc")
    ;; (define-auto-insert "\.cc" "template.cc")
    ;; (define-auto-insert "\.sh" "template.sh")
    ;; (define-auto-insert "\.py" "template.py")
