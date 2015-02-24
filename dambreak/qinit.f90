
subroutine qinit(meqn,mbc,mx,my,xlower,ylower,dx,dy,q,maux,aux)
    
    use qinit_module, only: qinit_type,add_perturbation
    use geoclaw_module, only: sea_level
    
    implicit none
    
    ! Subroutine arguments
    integer, intent(in) :: meqn,mbc,mx,my,maux
    real(kind=8), intent(in) :: xlower,ylower,dx,dy
    real(kind=8), intent(inout) :: q(meqn,1-mbc:mx+mbc,1-mbc:my+mbc)
    real(kind=8), intent(inout) :: aux(maux,1-mbc:mx+mbc,1-mbc:my+mbc)
    common /comic/ sloc,hl,ul,hr,ur
    
    ! Locals
    integer :: i,j,m
    real(kind=8) :: discharge
    
    ! Set flat state based on sea_level
    q = 0.d0
    !discharge = 0.115d0 * 0.054  ! free stream
    do i=1,mx
        xcenter = xlower + (i - 0.5d0) * dx
        do j=1,my
            if (xcenter < sloc) then
                q(1,i,j) = hl
                q(2,i,j) = hl*ul
            else
                q(1,i,j) = hr
                q(2,i,j) = hr*ur
            endif
        enddo
    enddo

!The grammar below seem to be incorrect for *.f90. It's only correct fo *.f
!    forall(i=1:mx, j=1:my)
!        xcenter = xlower + (i - 0.5d0) * dx
!        if (xcenter < sloc) then
!            q(1,i,j) = hl
!            q(2,i,j) = hl*ul
!        else
!            q(1,i,j) = hr
!            q(2,i,j) = hr*ur
!        !q(1,i,j) = max(0.d0, sea_level - aux(1,i,j))
!        !q(2,i,j) = discharge   ! 0.115d0 * q(1,i,j)
!        endif
!    end forall

end subroutine qinit
