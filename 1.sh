_wudao() 
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="--help --kill --short-desc"
    optl="
the
admitting
"

    if [[ ${cur} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    else
        COMPREPLY=( $(compgen -W "${optl}" -- ${cur}) )
        return 0
    fi
}
complete -F _wudao wd

